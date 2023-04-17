class cuentas():

    def __init__(self, id, nombre=None, saldo=None, telefono=None, cuenta=None) -> None:
        self.id       = id
        self.nombre   = nombre
        self.cuenta   = cuenta
        self.saldo    = saldo
        self.telefono = telefono
    
   
    def to_JSON(self):
        return {
            'id'       : self.id,
            'nombre'   : self.nombre,
            'cuenta'   : self.cuenta,
            'saldo'    : self.saldo,
            'telefono' : self.telefono
        }