import instaloader

L = instaloader.Instaloader(
    download_comments=False,
    download_geotags=False,
    download_video_thumbnails=False,
    save_metadata=False,

)

#Replace with Actual Link
url = "https://www.instagram.com/reel/DO-KjMHgQug/?igsh=MTFiNDI4cXc3cGJubA=="

shortcode = url.split('/')[-2]

try:
        # Get the Post object for the reel
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        # Download the reel
        L.download_post(post, target=shortcode) # Reels will be saved in a 'downloads' folder
        print(f"Reel with shortcode '{shortcode}' downloaded.")

except Exception as e:
        print(f"Error downloading reel: {e}")