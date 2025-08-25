#!/usr/bin/env python3
# Required parameters:
# @wox.id wox-60s-news
# @wox.name 每日 60 秒新闻
# @wox.keywords 60s
#
# Optional parameters:
# @wox.icon base64:data:image/jpeg;base64,/9j/2wCEAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDIBCQkJDAsMGA0NGDIhHCEyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMv/AABEIADAAMAMBIgACEQEDEQH/xAGiAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgsQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+gEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoLEQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/AO886MdWA9zxTwQRkc0pHNM2xpl9qrgctjFfCH0VyB79FlmjVHdolZnCYJCqoZmIzwMEfXoKtA5rlrnSop7uTUrezna8l2lVUboz8oG4naeO2AecdOajsbi8k1yEz3N1lS7Sq4McaoFOcLwMAleTk89a9KWCvT546WWt+vocyre9ZnUiUGZowCdoBJ9PapKx7LWEub4xQwN5DsdszNy59lx046n8q2K4KlKdN2mrG8ZKWwVy+sapqMOvQ26wK2nxmOSYcbpF3AsMHqCAQAOpzk1peI1mk0aWKCcwPKQgkXOV/Ij6de9U/DvhqbUrSWOWb5YZQsUxJ3qCoLYHTb7HuM9ea9HLsPf961fy/U58RUsuTYg+KWna9rcFlNoV/wCRCNkqy+aYlI+bJ3/wn7p5IzxjO2sTWvElzoPh5XuoIdUFpHGqtJGR8xCK5BIyELhjgjGNowMjHsk81npVg007xwWsQ5J4AH/6z+NZ0FnoOu2purWOKRGyDJGCh5xkEccHg4IweDjpX0d+jPLS6nDaCBqfhqHxBaW32HbC1zJb7iRsJdSQWzyNrEDoRt6ZxXS26SJAiSuHcDBIB5/MmuI1lNS1BfIsZrwksRtAlRXXaQOen93lsgAY6cV29usi28azMGlCAOw6E45NeBm3I3Fx3PRwnMlZhcQJcwNE4+Vh+XvTvD9x/Y5ktryNisr7kniBZenRhjK/Xke4p9FcGGxdTDv3djoq0Y1FqR+KxNq3h60lSAsq3AaeKNt5VSjr/D15ZT7de1Ytkh8L+Gbi3AMM984it4ZHJbYB8znJznk/+O1u7cNuBKt/eUkH8xTfKTzjMV3SkYMjcsR6ZPNej/a6cdY6+pzfU3fc5/z9WuDlfNC9kjiCL+bc/rVzT4NQW4Dzs6x4+ZXk3E/zrXorzp4rmi4qKS9DpjStrc//2Q==
# @wox.version 1.0.0
# @wox.author qianlifeng
# @wox.description 基于 https://60s.viki.moe/v2/60s 的每日新闻展示
# @wox.minWoxVersion 2.0.0

# English comments for code, per your preference.

import json
import sys
import urllib.request
import urllib.error
import os
from typing import Any, Dict, List, Tuple

API_URL = "https://60s.viki.moe/v2/60s"
ICON = 'base64:data:image/jpeg;base64,/9j/2wCEAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDIBCQkJDAsMGA0NGDIhHCEyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMv/AABEIADAAMAMBIgACEQEDEQH/xAGiAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgsQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+gEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoLEQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/AO886MdWA9zxTwQRkc0pHNM2xpl9qrgctjFfCH0VyB79FlmjVHdolZnCYJCqoZmIzwMEfXoKtA5rlrnSop7uTUrezna8l2lVUboz8oG4naeO2AecdOajsbi8k1yEz3N1lS7Sq4McaoFOcLwMAleTk89a9KWCvT546WWt+vocyre9ZnUiUGZowCdoBJ9PapKx7LWEub4xQwN5DsdszNy59lx046n8q2K4KlKdN2mrG8ZKWwVy+sapqMOvQ26wK2nxmOSYcbpF3AsMHqCAQAOpzk1peI1mk0aWKCcwPKQgkXOV/Ij6de9U/DvhqbUrSWOWb5YZQsUxJ3qCoLYHTb7HuM9ea9HLsPf961fy/U58RUsuTYg+KWna9rcFlNoV/wCRCNkqy+aYlI+bJ3/wn7p5IzxjO2sTWvElzoPh5XuoIdUFpHGqtJGR8xCK5BIyELhjgjGNowMjHsk81npVg007xwWsQ5J4AH/6z+NZ0FnoOu2purWOKRGyDJGCh5xkEccHg4IweDjpX0d+jPLS6nDaCBqfhqHxBaW32HbC1zJb7iRsJdSQWzyNrEDoRt6ZxXS26SJAiSuHcDBIB5/MmuI1lNS1BfIsZrwksRtAlRXXaQOen93lsgAY6cV29usi28azMGlCAOw6E45NeBm3I3Fx3PRwnMlZhcQJcwNE4+Vh+XvTvD9x/Y5ktryNisr7kniBZenRhjK/Xke4p9FcGGxdTDv3djoq0Y1FqR+KxNq3h60lSAsq3AaeKNt5VSjr/D15ZT7de1Ytkh8L+Gbi3AMM984it4ZHJbYB8znJznk/+O1u7cNuBKt/eUkH8xTfKTzjMV3SkYMjcsR6ZPNej/a6cdY6+pzfU3fc5/z9WuDlfNC9kjiCL+bc/rVzT4NQW4Dzs6x4+ZXk3E/zrXorzp4rmi4qKS9DpjStrc//2Q=='

def fetch_60s() -> Tuple[Dict[str, Any], str]:
    """Fetch 60s news JSON. Returns (data, error)."""
    try:
        req = urllib.request.Request(
            API_URL,
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=6) as resp:
            text = resp.read().decode("utf-8", errors="ignore")
            obj = json.loads(text)
            if not isinstance(obj, dict):
                return {}, "Invalid JSON root"
            if obj.get("code") != 200:
                return {}, f"API error: code={obj.get('code')}"
            data = obj.get("data", {})
            if not isinstance(data, dict):
                return {}, "Invalid data payload"
            return data, ""
    except urllib.error.URLError as e:
        return {}, f"Network error: {e}"
    except Exception as e:
        return {}, f"Unexpected error: {e}"

def build_items(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Build Wox result items from API data."""
    news_list = data.get("news") or []

    items: List[Dict[str, Any]] = []

    for n in news_list:
        if not isinstance(n, str):
            continue
        items.append({
            "title": n.strip(),
            "icon": ICON,
        })

    return items

def handle_query(params: Dict[str, Any], request_id: Any) -> Dict[str, Any]:
    """Handle query request."""
    data, err = fetch_60s()
    if err:
        return {
            "jsonrpc": "2.0",
            "result": {"items": [{
            "title": "获取 60s 新闻失败",
            "subtitle": err,
        }]},
            "id": request_id
        }

    items = build_items(data)
    return {
        "jsonrpc": "2.0",
        "result": {"items": items},
        "id": request_id
    }

def main() -> int:
    """Main entry point for the script plugin."""
    # Read JSON-RPC request from argv or stdin
    try:
        if len(sys.argv) > 1:
            request = json.loads(sys.argv[1])
        else:
            request = json.loads(sys.stdin.read())
    except json.JSONDecodeError as e:
        print(json.dumps({
            "jsonrpc": "2.0",
            "error": {"code": -32700, "message": "Parse error", "data": str(e)},
            "id": None
        }))
        return 1

    if request.get("jsonrpc") != "2.0":
        print(json.dumps({
            "jsonrpc": "2.0",
            "error": {"code": -32600, "message": "Invalid Request", "data": "Expected JSON-RPC 2.0"},
            "id": request.get("id")
        }))
        return 1

    method = request.get("method")
    params = request.get("params", {}) or {}
    req_id = request.get("id")

    if method == "query":
        response = handle_query(params, req_id)
    else:
        response = {
            "jsonrpc": "2.0",
            "error": {"code": -32601, "message": "Method not found", "data": f"Method '{method}' not supported"},
            "id": req_id
        }

    print(json.dumps(response, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())