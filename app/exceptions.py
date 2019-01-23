""" Inicio das exceções referentes ao dominio de Kindness. """

class UploadImageException(Exception):
    pass


class CreateKindnessException(Exception):
    pass


class UpdateKindnessException(Exception):
    pass

""" Fim das exceções referentes ao dominio de Kindness."""


""" Inicio das exceções referentes ao dominio de Usuário """
class CreateAccountException(Exception):
    pass


class LoginException(Exception):
    pass


class UpdateProfileException(Exception):
    pass
