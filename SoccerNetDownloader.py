import SoccerNet

from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="SoccerNetData")
mySoccerNetDownloader.password = ""
mySoccerNetDownloader.downloadGames(files=["1_224p.mkv", "2_224p.mkv"], split=["train","valid","test","challenge"])
# mySoccerNetDownloader.downloadGames(files=["1_ResNET_TF2_PCA512.npy", "2_ResNET_TF2_PCA512.npy"], split=["train","valid","test","challenge"])
# mySoccerNetDownloader.downloadGames(files=["1_baidu_soccer_embeddings.npy", "2_baidu_soccer_embeddings.npy"], split=["train","valid","test","challenge"])
# mySoccerNetDownloader.downloadGames(files=["Frames-v3.zip"], split=["train","valid","test"], task="frames")
# mySoccerNetDownloader.downloadGames(files=["Labels-v2.json"], split=["train","valid","test"])
# mySoccerNetDownloader.downloadGames(files=["Labels-cameras.json"], split=["train","valid","test"])
# mySoccerNetDownloader.downloadDataTask(task="calibration", split=["train","valid","test","challenge"]) 
# mySoccerNetDownloader.downloadDataTask(task="calibration-2023", split=["train","valid","test","challenge"])
# mySoccerNetDownloader.downloadDataTask(task="reid", split=["train", "valid", "test", "challenge"])
# mySoccerNetDownloader.downloadDataTask(task="reid-2023", split=["train", "valid", "test", "challenge"])
# mySoccerNetDownloader.downloadDataTask(task="tracking", split=["train", "test", "challenge"])
# mySoccerNetDownloader.downloadDataTask(task="tracking-2023", split=["train", "test", "challenge"])
# mySoccerNetDownloader.downloadDataTask(task="caption-2023", split=["train","valid", "test","challenge"])
# mySoccerNetDownloader.downloadDataTask(task="spotting-ball-2023", split=["train", "valid", "test", "challenge"], password="")