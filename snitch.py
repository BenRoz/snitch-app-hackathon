from bottle import route, run, template, static_file, get, post, delete, request, BaseRequest
from sys import argv
import json
import pymysql

BaseRequest.MEMFILE_MAX=1024*1024

# connection = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='bensql',
#     db='ben_online_store',
#     charset='utf8',
#     cursorclass=pymysql.cursors.DictCursor
# )

@get("/")
def index():
    print "in index"
    return template("index.html")


@post("/data")
def send_data():
    time_stamp = request.POST.get('time')
    location = request.POST.get('location')
    image = request.POST.get('image')
    user_info = request.POST.get('user_info')
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO catagory (user_info, location, time, image ) VALUES ("{}")'.format()
            cursor.execute(sql)
            cat_id = cursor.lastrowid
            connection.commit()
            status = "success"
            msg=""
            print "success code category created - 201"

    except Exception as e:
        status = "error"
        msg = repr(e)
        cat_id=0
    result = {"STATUS": status, "CAT_ID": cat_id, "MSG": msg}
    return json.dumps(result)

@post("/image")
def get_img():
    image = request.POST.get('imgBase64')
    #functiuon of datasciene guys
    print image
    #return image
    return "Saved"

@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')

@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')

@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')

def main():
    run(host='localhost', port=7009)

if __name__ == '__main__':
    main()
