import urllib.error
import time
import types

from SoccerNet.Downloader import SoccerNetDownloader

mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="/ml/public_data/soccernet")
mySoccerNetDownloader.password = "s0cc3rn3t"

_original_downloadFile = SoccerNetDownloader.downloadFile

def _downloadFile_with_retry(self, path_local, path_owncloud, user=None, password=None, verbose=True):
    max_retries = 10
    for attempt in range(max_retries):
        try:
            return _original_downloadFile(self, path_local, path_owncloud, user=user, password=password, verbose=verbose)
        except urllib.error.ContentTooShortError:
            if attempt < max_retries - 1:
                wait = 2 ** min(attempt, 5)  # exponential backoff, capped at 32s
                print(f"\nIncomplete download, retrying in {wait}s (attempt {attempt + 2}/{max_retries})...")
                time.sleep(wait)
            else:
                print(f"\nFailed after {max_retries} attempts: {path_local}")
                raise

mySoccerNetDownloader.downloadFile = types.MethodType(_downloadFile_with_retry, mySoccerNetDownloader)

mySoccerNetDownloader.downloadGames(files=["1_720p.mkv", "2_720p.mkv"], split=["train","valid","test","challenge"])
# mySoccerNetDownloader.downloadGames(files=["1_224p.mkv", "2_224p.mkv"], split=["train","valid","test","challenge"])