import json
import requests


def parse_json(json_data):
    json_dict = json.loads(json_data)
    return json_dict


def import_video_data(URL):
    print('Fetching Video page source using URL ' + URL)
    # window["ytInitialData"] =
    page_source = requests.get(URL)
    page_source = page_source.text
    start_index = page_source.find('ytInitialData')
    tmp = page_source[ start_index+17:]
    end_index = tmp.find('}};')
    tmp = tmp[:end_index] + '}}'
    return tmp


def main():
    print('MAIN')
    json_data = import_video_data(URL='https://www.youtube.com/watch?v=JRtgXN-bwGE')
    yt_json = parse_json(json_data)

    video_id = yt_json['currentVideoEndpoint']['watchEndpoint']['videoId']
    print('VideoId:' + video_id)

    title = \
        yt_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer'][
            'title']['runs'][0]['text']
    print('Title:'+ title)

    views = \
        yt_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer'][
            'viewCount']['videoViewCountRenderer']['viewCount']['simpleText']
    short_views = \
        yt_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer'][
            'viewCount']['videoViewCountRenderer']['shortViewCount']['simpleText']
    print('Views:' + views + ' in short:'+ short_views)

    likes = \
        yt_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer'][
            'videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']['accessibility'][
            'accessibilityData']['label']
    likes_inshort = \
        yt_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer'][
            'videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']['simpleText']
    print('Likes:'+ likes+' in short:'+ likes_inshort)

    dislikes = \
        yt_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer'][
            'videoActions']['menuRenderer']['topLevelButtons'][1]['toggleButtonRenderer']['defaultText']['accessibility'][
            'accessibilityData']['label']
    dislikes_inshort = \
        yt_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer'][
            'videoActions']['menuRenderer']['topLevelButtons'][1]['toggleButtonRenderer']['defaultText']['simpleText']
    print('Dis-Likes:'+ dislikes+' in short:'+ dislikes_inshort)


    published_date = \
        yt_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer'][
            'dateText']['simpleText']
    print('Published Date:'+ published_date)


if __name__ == '__main__':
    main()