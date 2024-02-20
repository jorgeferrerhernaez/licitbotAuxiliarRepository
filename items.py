# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
 
import scrapy
 
 
class BusquedaLicitacionesItem(scrapy.Item): # ver si sobra
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
 
class Licitacion(scrapy.Item):
    #expediente, descripción, tipo de contrato, estado, importe, fecha limite, organo de contratacion
    url = scrapy.Field()
    titulo = scrapy.Field()
    descripcion = scrapy.Field()
    tipo_contrato = scrapy.Field()
    estado = scrapy.Field()
    importe = scrapy.Field()
    presentacion = scrapy.Field()
    organo_contratacion = scrapy.Field()
    pass
 
class Licitacion_avanzado(scrapy.Item):
    #expediente, descripción, tipo de contrato, estado, importe, fecha limite, organo de contratacion
    Url = scrapy.Field()
    Titulo_expediente = scrapy.Field()
    Descripcion = scrapy.Field()
    Tipo_contrato = scrapy.Field()
    Estado = scrapy.Field()
    Importe = scrapy.Field()
    Fechas = scrapy.Field()
    Organo_contratacion = scrapy.Field()
    pass
 
 