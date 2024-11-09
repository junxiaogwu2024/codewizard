import web
from Models import RegisterModel, LoginModel, PostModel
import os
web.config.debug = False

urls = (
    '/', 'Home',
    '/login', 'Login',
    '/logout', 'Logout',
    '/register', 'Register',
    '/postregistration', 'PostRegistration',
    '/checklogin', 'CheckLogin',
    '/postactivity', 'PostActivity',
    '/info', 'UserInfo',
    '/settings', 'Settings',
    '/update-settings', 'UpdateSettings',
    '/profile', 'UserProfile',
    '/upload-image/background', 'UploadBackground',
    '/upload-image/avatar', 'UploadAvatar'
)


app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user':None} )
session_data = session._initializer

render = web.template.render('Views/Templates', base="MainLayout", globals={'session': session_data, 'current_user': session_data['user']})

#Classes/Routes


class Home:
    def GET(self):
        data = type('obj', (object,), {"username": "Happy1", "password": "Blockchain1"})

        login = LoginModel.LoginModel()
        isCorrect = login.check_login(data)
        if isCorrect:
            session_data['user'] = isCorrect

        post_model = PostModel.PostModel()
        posts = post_model.get_all_posts()

        return render.Home(posts)


class Login:
    def GET(self):
        return render.Login()


class Register:
    def GET(self):
        return render.Register()


class PostRegistration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)

        return data.username


class CheckLogin:
    def POST(self):
        data = web.input()
        login_model = LoginModel.LoginModel()
        isCorrect = login_model.check_login(data)

        if isCorrect:
            session_data['user'] = isCorrect
            return isCorrect

        return "error"


class UserInfo:
    def GET(self):
        return render.UserInfo()

class UserProfile:
    def GET(self):
        return render.Profile()


class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        post_model = PostModel.PostModel()
        new_post = post_model.insert_post(data)
        return "success"


class Settings:
    def GET(self):
        return render.Settings()


class UpdateSettings:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        settings_model = LoginModel.LoginModel()
        if settings_model.update_info(data):
            return "Success"
        else:
            return "Error on updating settings"

class UploadAvatar:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        settings_model = LoginModel.LoginModel()
        if settings_model.update_image(data):
            return "Success"
        else:
            return "Error on updating avatar"

class Logout:
    def GET(self):
        session_data['user'] = None
        session.kill()
        return "Success"


class UploadBackground:
    def POST(self):
        file = web.input()
        print("Background is ", file.items())

        filename = ""
        for k in file.items():
            print(k[0])
            filename = k[0] + ".jpg"

        print(filename)

        file_dir = os.getcwd() + "/static/uploads/" + session_data['user']['username']

        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        if "avatar" or "background" in file:

            f = open(file_dir + "/" + filename, 'wb')
            f.write(file.get("background"))
            f.close()

            update = {}
            update["background"] = '/static/uploads/'+ session_data["user"]["username"] + "/" + filename
            update["username"] = session_data['user']['username']

            login_model = LoginModel.LoginModel()
            update_image = login_model.update_image(update)

        raise web.seeother("/settings")

class UploadAvatar:
    def POST(self):
        file = web.input()
        print("Avatar is ", file.items())

        filename = ""
        for k in file.items():
            print(k[0])
            filename = k[0] + ".jpg"

        print(filename)

        file_dir = os.getcwd() + "/static/uploads/" + session_data['user']['username']

        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        if "avatar" or "background" in file:

            f = open(file_dir + "/" + filename, 'wb')
            f.write(file.get("avatar"))
            f.close()

            update = {}
            update["avatar"] = '/static/uploads/'+ session_data["user"]["username"] + "/" + filename
            update["username"] = session_data['user']['username']

            login_model = LoginModel.LoginModel()
            update_image = login_model.update_image(update)

        raise web.seeother("/settings")

if __name__ == "__main__":
    app.run()