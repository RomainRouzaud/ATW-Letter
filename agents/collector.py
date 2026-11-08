import feedparser
import yaml
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

def load_sources(config_path="config/sources.yaml"):
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    sources = []
    if "sources" in config:
        sources.extend(config["sources"])
    elif "source_groups" in config:
        for group in config["source_groups"]:
            cat = group.get("category", "General")
            for src in group.get("sources", []):
                if src.get("enabled", True):
                    src["category"] = cat
                    sources.append(src)
    return sources

def clean_html(raw_html):
    if not raw_html:
        return ""
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text(separator=" ", strip=True)

def extract_entry_images(entry, raw_html):
    images = []
    seen_urls = set()

    # 1. Enclosures
    if hasattr(entry, 'enclosures'):
        for enc in entry.enclosures:
            if enc.get('type', '').startswith('image/') and enc.get('href'):
                href = enc['href']
                if href not in seen_urls:
                    images.append({'url': href, 'alt': entry.get('title', '')})
                    seen_urls.add(href)

    # 2. Media content (RSS media extension)
    if hasattr(entry, 'media_content'):
        for med in entry.media_content:
            href = med.get('url')
            if href and href not in seen_urls:
                images.append({'url': href, 'alt': entry.get('title', '')})
                seen_urls.add(href)

    # 3. HTML <img> tags
    if raw_html:
        soup = BeautifulSoup(raw_html, "html.parser")
        for img in soup.find_all("img"):
            src = img.get("src")
            if not src:
                continue
            src_lower = src.lower()
            # Ignore tracking pixels, analytics, badges, tiny icons, Medium stat beacons
            if any(bad in src_lower for bad in ['tracking', 'pixel', '1x1', 'gravatar', 'feedburner', 'beacon', 'badge', 'medium.com/_/stat', 'stat?', 'clientviewed']):
                continue
            if src in seen_urls:
                continue
            alt = img.get("alt", "").strip() or img.get("title", "").strip() or entry.get("title", "")
            images.append({'url': src, 'alt': alt})
            seen_urls.add(src)

    return images

import requests

def collect_daily_articles(sources):
    today = datetime.now().strftime("%Y-%m-%d")
    articles = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    for source in sources:
        print(f"Fetching {source['name']}...")
        try:
            res = requests.get(source['url'], headers=headers, timeout=10)
            if res.status_code != 200:
                print(f"Failed to fetch {source['name']}: HTTP {res.status_code}")
                continue
            feed = feedparser.parse(res.text)
            for entry in feed.entries:
                published = getattr(entry, "published", getattr(entry, "updated", "Unknown date"))
                raw_content = ""
                if "content" in entry:
                    raw_content = entry.content[0].value
                elif "summary" in entry:
                    raw_content = entry.summary
                
                clean_content = clean_html(raw_content)
                images = extract_entry_images(entry, raw_content)

                source_tags = source.get("tags", [])
                is_wardley = (
                    "wardley-maps" in source_tags
                    or "wardley" in source['name'].lower()
                    or "wardley" in entry.title.lower()
                    or "wardley map" in raw_content.lower()
                )
                is_gcp = (
                    "gcp" in source_tags
                    or "google-cloud" in source_tags
                    or "google cloud" in source['name'].lower()
                    or "gcp" in entry.title.lower()
                    or "google cloud" in entry.title.lower()
                    or "google cloud" in raw_content.lower()
                )
                is_ibm = (
                    "ibm-cloud" in source_tags
                    or "ibm" in source_tags
                    or "watsonx" in source_tags
                    or "ibm" in source['name'].lower()
                    or "watsonx" in source['name'].lower()
                    or "ibm" in entry.title.lower()
                    or "watsonx" in entry.title.lower()
                    or "ibm cloud" in raw_content.lower()
                )
                is_dev_agent = (
                    "developer-agents" in source_tags
                    or "augmented-developer" in source_tags
                    or any(t in source_tags for t in ["coding-agent", "copilot", "cursor", "swe-bench", "ai-coding", "ide-ai"])
                    or "developer agent" in source.get("category", "").lower()
                    or any(k in entry.title.lower() for k in [
                        "copilot", "cursor", "developer agent", "coding agent", "dev augmenté",
                        "augmented developer", "code generation", "pair programming", "swe-bench",
                        "claude code", "qodo", "codium", "continue.dev", "jetbrains ai"
                    ])
                    or any(k in raw_content.lower() for k in [
                        "developer agent", "coding agent", "augmented developer", "développeur augmenté", "agent développeur"
                    ])
                )
                
                article = {
                    "title": entry.title,
                    "link": entry.link,
                    "published": published,
                    "source": source['name'],
                    "category": source['category'],
                    "tags": source_tags,
                    "content": clean_content[:5000],
                    "images": images,
                    "has_wardley": is_wardley,
                    "is_gcp": is_gcp,
                    "is_ibm": is_ibm,
                    "is_dev_agent": is_dev_agent,
                    "fetch_date": today
                }
                articles.append(article)
                
                # To avoid overloading, just fetch the very latest 2 per source
                if len([a for a in articles if a['source'] == source['name']]) >= 2:
                    break
        except Exception as e:
            print(f"Error fetching {source['name']}: {e}")

    return articles

def save_raw_articles(articles, output_dir="data/raw"):
    os.makedirs(output_dir, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    filepath = os.path.join(output_dir, f"articles_{today}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    return filepath

if __name__ == "__main__":
    sources = load_sources()
    articles = collect_daily_articles(sources)
    saved_path = save_raw_articles(articles)
    print(f"Saved {len(articles)} articles to {saved_path}")
