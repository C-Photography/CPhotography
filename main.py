from website import create_app

app = create_app()#initialize cookie set/


#run application
if __name__=='__main__':
    app.run(debug=True)#reruns webserver while debugging server



