from marshmallow import Schema, fields, validate


class CreateUserSchema(Schema):

    documento = fields.Str(required=True, validate=validate.Length(
        min=7, max=15), data_key='documento')

    nombres = fields.Str(required=True, validate=validate.Length(
        min=3, max=25), data_key='nombres')

    apellidos = fields.Str(required=True, validate=validate.Length(
        min=3, max=25), data_key='apellidos')

    edad = fields.Str(
        required=True, validate=validate.Length(max=2), data_key='edad')

    correo = fields.Str(
        required=True, validate=validate.Email(), data_key='correo')

    ficha = fields.Str(required=True, validate=validate.Length(
        min=6, max=15), data_key='ficha')

    idprograma = fields.Integer(required=True, data_key='idprograma')

    tipouser = fields.Str(required=True, validate=validate.OneOf(
        ['admin', 'user']), data_key='tipouser')

    tipopersona = fields.Str(required=True, validate=validate.OneOf(
        ['Aprendiz', 'Funcionario']), data_key='tipopersona')

    jornada = fields.Str(required=True, validate=validate.Length(
        min=4, max=10), data_key='jornada')

    telefono = fields.Str(required=True, validate=validate.Length(
        min=7, max=10), data_key='telefono')


class CreateUserFuncionarioSchema(Schema):
    documento = fields.Str(required=True, validate=validate.Length(
        min=7, max=15), data_key='documento')

    nombres = fields.Str(required=True, validate=validate.Length(
        min=3, max=25), data_key='nombres')

    apellidos = fields.Str(required=True, validate=validate.Length(
        min=3, max=25), data_key='apellidos')

    edad = fields.Str(
        required=True, validate=validate.Length(max=2), data_key='edad')

    correo = fields.Str(
        required=True, validate=validate.Email(), data_key='correo')

    tipouser = fields.Str(required=True, validate=validate.OneOf(
        ['Aprendiz', 'Funcionario']), data_key='tipouser')

    tipopersona = fields.Str(required=True, validate=validate.OneOf(
        ['admin', 'user']), data_key='tipopersona')

    telefono = fields.Str(required=True, validate=validate.Length(
        min=7, max=10), data_key='telefono')


class ChangePasswordSchema(Schema):

    password = fields.Str(required=True, validate=validate.Length(min=6, max=256), data_key='password')
