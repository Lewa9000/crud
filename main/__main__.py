import uvicorn
 
from entities import app
from utils import parser, add_new_user
from controllers import *


def main(host: str='localhost', port: int=8000):
    uvicorn.run(app, host=host, port=port)


if __name__ == '__main__':
    args = parser.parse_args()
    if args.new_user:
        add_new_user()
    else:
        main()
