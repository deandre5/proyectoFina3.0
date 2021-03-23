from marshmallow import Schema, fields, validate

class actualizarUserSchema(Schema):
    nombres = fields.Str(required=True, validate=validate.Length(
        min=3, max=25), data_key='nombres')

    apellidos = fields.Str(required=True, validate=validate.Length(
        min=3, max=25), data_key='apellidos')

    edad = fields.Str(
        required=True, validate=validate.Length(max=2), data_key='edad')

    correo = fields.Str(
        required=True, validate=validate.Email(), data_key='correo')
    
    telefono = fields.Str(required=True, validate=validate.Length(
        min=7, max=10), data_key='telefono')


class actualizarUserSinFotoSchema(Schema):
    nombres = fields.Str(required=True, validate=validate.Length(
        min=3, max=25), data_key='nombres')

    apellidos = fields.Str(required=True, validate=validate.Length(
        min=3, max=25), data_key='apellidos')

    edad = fields.Str(
        required=True, validate=validate.Length(max=2), data_key='edad')

    correo = fields.Str(
        required=True, validate=validate.Email(), data_key='correo')
    
    telefono = fields.Str(required=True, validate=validate.Length(
        min=7, max=10), data_key='telefono')

    imagen = fields.Str(required=True)
