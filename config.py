
import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8074729076:AAE6umNu6OfvWajVNhyqMVUxoquyeY8lqZ8")
    API_ID = int(os.environ.get("API_ID", "26037262"))
    API_HASH = os.environ.get("API_HASH", "9b2cabc8b962945d05152d0fe5cbc37f")
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://gohilkanubhai1980:wZMjeJxxBPeu0VOn@cluster0.sbyxs3i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    AUTH_USERS = [7009468802, 7513565186, 6804641253, 7653322737]


