# youtube-search

Dockerized basic localized YouTube search

## To run

`docker-compose up` in root project dir

## To change search text for ingestion, change value in

`./content/services/youtube_service.py ln10 -> q variable`, currently set to `dogs`

## To access APIs

### For search video content

`http://localhost:8000/api/video/search/?text='replace text here under single quotes'`

sample call `http://localhost:8000/api/video/search/?text='dogs cats'`

### For adding/viewing youtube API token

`http://localhost:8000/api/youtube-token/`
use GET to view keys and their current status use POST to insert new keys (requires api_key)

### For adding/viewing video

`http://localhost:8000/api/video-details/`
use GET to get list of video details use POST to insert new video

### For adding/viewing video

`http://localhost:8000/api/video-thumbnail/`
use GET to get list of video thumbnails use POST to insert new video thumbnail

## Features

1. Ingestion script reuses youtube api_keys based on response - if api_key is expired, it will be reused again after 24
   hours based on logic
2. Integration with haystack allows django ORM like query style
3. Scripts run in a separate docker service - allows separation of processes to scale better
4. Optimised search to include partial match for the search query
5. Dashboard for viewing videos and video thumbnails
6. Add Multiple youtube `api_key`

## Future Scope

1. API response of search are not paginated
2. Ingestion currently does not support bringing back complete paginated data from youtube API
3. Better integration with DRF to allow easier search indexing
