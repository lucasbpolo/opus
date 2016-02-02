import os
import jinja2
import webapp2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

class QuemSomosPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('quemsomos.html')
        self.response.write(template.render())

class NossosObjetivosPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('nossosobjetivos.html')
        self.response.write(template.render())

class NossasAtividadesPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('nossasatividades.html')
        self.response.write(template.render())

class ProgramacaoPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('programacao.html')
        self.response.write(template.render())

class ArtigosPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos.html')
        self.response.write(template.render())

class NoticiasPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('noticias.html')
        self.response.write(template.render())

class FotosPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('fotos.html')
        self.response.write(template.render())

class a1(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos_-_A_PSICOTERAPIA_JUNGUIANA.html')
        self.response.write(template.render())

class a2(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos_-_A_CONSTRUCAO_DAS_RELACOES_FAMILIARES.html')
        self.response.write(template.render())

class a3(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos_-_Abordagem_Junguiana_e_Psicoterapia_Breve_uma_integracao_possivel.html')
        self.response.write(template.render())

class a4(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos_-_sozinhos_na_multidao.html')
        self.response.write(template.render())

class a5(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos_-_A_ANSIEDADE_COMO_TEMA_DA_MODERNIDADE.html')
        self.response.write(template.render())

class a6(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos_-_psicologia_e_religiao.html')
        self.response.write(template.render())

class a7(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos_-_adaptacao.html')
        self.response.write(template.render())

class a8(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos_-_a_crise_e_seus.html')
        self.response.write(template.render())

class a9(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos_-_abordagem_focal.html')
        self.response.write(template.render())

class a10(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos_-_oscontosdefadas.html')
        self.response.write(template.render())

class a11(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos-1.html')
        self.response.write(template.render())

class a12(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos_-_sobre_a_mitologia.html')
        self.response.write(template.render())

class a13(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos_-_mitosdacriacao.html')
        self.response.write(template.render())

class a14(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos_-_A_PARABOLA_DO_FILHO_PRODIGO.html')
        self.response.write(template.render())

class a15(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos_-_familiamoderna.html')
        self.response.write(template.render())

class a16(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos-2.html')
        self.response.write(template.render())

class a17(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('artigos-3.html')
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/index.html', MainPage),
    ('/quemsomos.html', QuemSomosPage),
    ('/nossosobjetivos.html', NossosObjetivosPage),
    ('/nossasatividades.html', NossasAtividadesPage),
    ('/programacao.html', ProgramacaoPage),
    ('/artigos.html', ArtigosPage),
    ('/noticias.html', NoticiasPage),
    ('/fotos.html', FotosPage),
    ('/artigos_-_A_PSICOTERAPIA_JUNGUIANA.html', a1),
    ('/artigos_-_A_CONSTRUCAO_DAS_RELACOES_FAMILIARES.html', a2),
    ('/artigos_-_Abordagem_Junguiana_e_Psicoterapia_Breve_uma_integracao_possivel.html', a3),
    ('/artigos_-_sozinhos_na_multidao.html', a4),
    ('/artigos_-_A_ANSIEDADE_COMO_TEMA_DA_MODERNIDADE.html', a5),
    ('/artigos_-_psicologia_e_religiao.html', a6),
    ('/artigos_-_adaptacao.html', a7),
    ('/artigos_-_a_crise_e_seus.html', a8),
    ('/artigos_-_abordagem_focal.html', a9),
    ('/artigos_-_oscontosdefadas.html', a10),
    ('/artigos-1.html', a11),
    ('/artigos_-_sobre_a_mitologia.html', a12),
    ('/artigos_-_mitosdacriacao.html', a13),
    ('/artigos_-_A_PARABOLA_DO_FILHO_PRODIGO.html', a14),
    ('/artigos_-_familiamoderna.html', a15),
    ('/artigos-2.html', a16),
    ('/artigos-3.html', a17),
    
], debug=True)