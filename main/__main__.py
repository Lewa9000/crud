import uvicorn
 
from entities import app
from controllers import *

def main(host: str='localhost', port: int=8000):
    uvicorn.run(app, host=host, port=port)

if __name__ == '__main__':
    main()
