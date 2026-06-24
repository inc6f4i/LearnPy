import requests
import json

def get_naver_maps_photos(business_id):
    # 네이버 플레이스 소식(Feed)을 가져오는 실제 내부 비공식 API 주소
    url = f"https://m.api.naver.com/virtual-place/v1/graphql"
    
    # 서버에 보낼 요청 데이터 (GraphQL 형태)
    payload = [{
        "operationName": "getFeedList",
        "variables": {
            "input": {
                "businessId": business_id,
                "deviceType": "pc",
                "page": 1,
                "size": 10
            }
        },
        "query": """query getFeedList($input: FeedListInput!) {
            feedList(input: $input) {
                edges {
                    node {
                        id
                        contents
                        images {
                            url
                        }
                    }
                }
            }
        }"""
    }]
    
    # 봇(Bot) 차단을 우회하기 위한 브라우저 흉내 헤더 설정
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Referer": f"https://map.naver.com/p/entry/place/{business_id}"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        feeds = data[0]['data']['feedList']['edges']
        
        image_urls = []
        
        # 최신 공지글(첫 번째 피드)에서 이미지 추출
        if feeds:
            latest_feed = feeds[0]['node']
            print(f"최신 공지 내용 요약: {latest_feed['contents'][:30]}...")
            
            for img in latest_feed.get('images', []):
                origin_url = img['url']
                # 원본 또는 큰 이미지를 얻기 위해 쿼리스트링 치환 (?type=f282_282 -> ?type=w1500)
                if "?type=" in origin_url:
                    large_url = origin_url.split("?")[0] + "?type=w1500"
                else:
                    large_url = origin_url
                
                image_urls.append(large_url)
        
        print(f"\n총 {len(image_urls)}개의 큰 이미지 주소를 찾았습니다:")
        for i, img_url in enumerate(image_urls, 1):
            print(f"이미지 {i}: {img_url}")
            
        return image_urls

    except Exception as e:
        print(f"데이터를 가져오는 중 오류 발생: {e}")

# 주소창의 플레이스 고유 ID (미래로한식당: 1756035066)
PLACE_ID = "1756035066"
get_naver_maps_photos(PLACE_ID)