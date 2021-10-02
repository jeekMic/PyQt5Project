from PyQt5 import QtWebEngineWidgets

class WebEngineView(QtWebEngineWidgets.QWebEngineView):

    def createWindow(self,QWebEnginePage_WebWindowType):
        page = WebEngineView(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    def on_url_changed(self,url):
        self.setUrl(url)
