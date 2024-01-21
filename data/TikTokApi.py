import requests


def get_tiktok_data(video_url):
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url": video_url}

    headers = {
        "X-RapidAPI-Key": "1f4b3d5519msh9e8ef05e5d28843p1bf66cjsn4489cf42decd",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json().get('video')[0]
    music_data = response.json().get('music')[0]
    return {"video": data, "music": music_data}

if __name__ == "__main__":
    from pprint import pprint
    pprint(get_tiktok_data('https://www.tiktok.com/@khalijohn_tt/video/7300576214383742209?_r=1&u_code=0&preview_pb=0&sharer_language=en&_d=ebighe0916mmfm&share_item_id=7300576214383742209&source=h5_m&timestamp=1705681114&social_share_type=0&utm_source=copy&utm_campaign=client_share&utm_medium=android&share_iid=7324278239198922503&share_link_id=0a63f070-b092-4dc9-9400-d76f2216d7a7&share_app_id=1233&ugbiz_name=MAIN&ug_btm=b2001&enable_checksum=1'))

