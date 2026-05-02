from fastapi import FastAPI
import time
# import asyncio
# import uvicorn
# from uvicorn.config import Config
# from uvicorn.server import Server
# from concurrent.futures import ThreadPoolExecutor

app = FastAPI()


@app.get('/')
def get_user_info():
    print("hello /")
    # time.sleep(10)
    print("bye /")
    return {
        'message': 'Success',
        'users': [
            {
                'name': 'test'
            }
        ]
    }


# @app.get('/greet')
# def get_user_info(name, age:int=8):
#     # print("hello")
#     # time.sleep(10)
#     # print("bye")
#     return {
#         'message': 'Success',
#         'users': [
#             {
#                 'name': f'Greeting for Mr. {name} with {age}'
#             }
#         ]
#     }

# if __name__ == '__main__':
#     executor = ThreadPoolExecutor(max_workers=1)
#     config = Config(app=app, host='0.0.0.0', port=8000, loop='asyncio', lifespan='on', workers=1)
#     server = Server(config=config)
#     server.run()


# from fastapi import FastAPI
# import time
# import threading
# import asyncio

# app = FastAPI()
# lock = threading.Lock()

# @app.get("/")
# async def get_user_info():
#     with lock:
#         print("hello /")
#         await asyncio.sleep(10)
#         print("bye /")
#         return {
#             'message': 'Success',
#             'users': [{'name': 'test'}]
#         }
