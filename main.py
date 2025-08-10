import spotipy
from spotipy.oauth2 import SpotifyOAuth
import flet as ft
import os

#認証情報を入力
print("Spotifyの認証情報を入力してください。")
print("Client ID:")
client_id = input().strip()
print("Client Secret:")
client_secret = input().strip()
print("Redirect URI:")
redirect_uri = input().strip()
# 環境変数に設定
os.environ["SPOTIPY_CLIENT_ID"] = client_id
os.environ["SPOTIPY_CLIENT_SECRET"] = client_secret
os.environ["SPOTIPY_REDIRECT_URI"] = redirect_uri
# Spotipyの認証設定
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-read-private",
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri
))

# Fletアプリのメイン関数
def main(page: ft.Page):
    
    page.title = "Spotify Playlist Fetcher"
    page.window.width = 490
    page.window.height = 490
    page.window.min_width = 490
    page.window.min_height = 490
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

#テキストフォームとドロップダウンメニュー

    url_input = ft.TextField(label="Enter Spotify Playlist URL", width=400)
    result_text = ft.Text()
    select_service_from = ft.Dropdown(
        options=[
            ft.dropdown.Option("Spotify"),
            ft.dropdown.Option("YouTube"),
            ft.dropdown.Option("Apple Music"),
            ft.dropdown.Option("Amazon Music")
        ],
        label="Select Service",
        width=400,
        value="Spotify"  # 初期値
    )
    text = ft.Text("To")
    select_serviceTO = ft.Dropdown(
        options=[
            ft.dropdown.Option("Spotify"),
            ft.dropdown.Option("YouTube"),
            ft.dropdown.Option("Apple Music"),
            ft.dropdown.Option("Amazon Music")
        ],
        label="Select Service",
        width=400,
        value="YouTube"  # 初期値
    )
    # プレイリストの内容を変数に格納する関数
    def fetch_playlist(_):
        url = url_input.value
        service_from = select_service_from.value
        service_to = select_serviceTO.value

        if not url:
            result_text.value = "URLを入力してください。"
            page.update()
            return
        if not service_from or not service_to:
            result_text.value = "サービスを選択してください。"
            page.update()
            return

        # 仮の処理: URLとサービスを表示
        result_text.value = f"Fetching playlist from {service_from} to {service_to} using URL: {url}"

        # プレイリスト内容を変数に格納しprint
        playlist_tracks = []
        if service_from == "Spotify" and url:
            # SpotifyのプレイリストID抽出
            playlist_id = None
            if "playlist/" in url:
                try:
                    playlist_id = url.split("playlist/")[1].split("?")[0]
                except Exception:
                    playlist_id = None
            elif "open.spotify.com" in url:
                try:
                    playlist_id = url.split("/")[-1].split("?")[0]
                except Exception:
                    playlist_id = None

            if playlist_id:
                try:
                    playlist = sp.playlist_tracks(playlist_id)
                    for item in playlist.get("items", []):
                        track = item.get("track")
                        if track:
                            name = track.get("name", "")
                            artists = ", ".join([a.get("name", "") for a in track.get("artists", [])])
                            playlist_tracks.append(f"{name} - {artists}")
                    print("Playlist tracks:", playlist_tracks)
                except Exception as e:
                    print("Error fetching playlist:", e)
            else:
                print("Invalid Spotify playlist URL.")

        # ページの更新
        page.update()
    fetch_button = ft.ElevatedButton(text="Fetch Playlist", on_click=fetch_playlist)
    page.add(url_input, result_text, select_service_from, text, select_serviceTO, fetch_button)
    # ページの更新
    page.update()

def export_apple_music  ():
    # Apple Musicを検索する処理を追加予定
    
    return


# Fletアプリを起動
if __name__ == "__main__":
    ft.app(target=main)