# Spotify Playlist Converter

Spotifyなどの音楽サービス間でプレイリストを変換・取得するためのGUIアプリケーションです。  
FletとSpotipyを使用しており、Spotifyのプレイリスト内容を取得できます。

## 必要環境

- Python 3.8以上
- [Flet](https://flet.dev/)
- [Spotipy](https://spotipy.readthedocs.io/)

## インストール

```bash
pip install flet spotipy
```

## 環境変数の設定

Spotify APIの認証情報を環境変数で設定してください。

- `SPOTIPY_CLIENT_ID`
- `SPOTIPY_CLIENT_SECRET`

例（Windowsコマンドプロンプト）:

```cmd
set SPOTIPY_CLIENT_ID=あなたのクライアントID
set SPOTIPY_CLIENT_SECRET=あなたのクライアントシークレット
```

## 使い方

1. アプリを起動します。
2. 変換元・変換先サービスを選択します（現状Spotifyのみ対応）。
3. SpotifyプレイリストのURLを入力し、「Fetch Playlist」ボタンを押します。
4. プレイリスト内容がコンソールに出力されます。

## 注意事項

- Spotify以外のサービスは今後対応予定です。
- 認証情報は漏洩しないようご注意ください。

## ライセンス

MIT License

---

# Spotify Playlist Converter (English)

A GUI application for converting and retrieving playlists between music services such as Spotify.  
Built with Flet and Spotipy, it currently supports fetching playlist contents from Spotify.

## Requirements

- Python 3.8 or higher
- [Flet](https://flet.dev/)
- [Spotipy](https://spotipy.readthedocs.io/)

## Installation

```bash
pip install flet spotipy
```

## Setting Environment Variables

Set your Spotify API credentials as environment variables:

- `SPOTIPY_CLIENT_ID`
- `SPOTIPY_CLIENT_SECRET`

Example (Windows Command Prompt):

```cmd
set SPOTIPY_CLIENT_ID=your_client_id
set SPOTIPY_CLIENT_SECRET=your_client_secret
```

## Usage

1. Launch the application.
2. Select the source and target services (currently only Spotify is supported).
3. Enter a Spotify playlist URL and click the "Fetch Playlist" button.
4. The playlist contents will be printed to the console.

## Notes

- Support for services other than Spotify is planned for the future.
- Please keep your authentication credentials secure.

## License

MIT License
