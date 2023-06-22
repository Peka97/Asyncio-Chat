import dis


class ClientVerifier(type):
    prohibited_methods = ['accept', 'listen']
    _TCP = {
        'AF_INET': False,
        'SOCK_STREAM': False
    }

    def __init__(self, clsname, bases, clsdict):
        for key, value in clsdict.items():
            value = str(value)
            if '<socket.socket' in value:
                raise TypeError(
                    f'Forbidden attr: {key} - {value}'
                )

        for func in clsdict:
            try:
                instractions = dis.get_instructions(clsdict[func])
            except TypeError:
                pass
            else:
                for inst in instractions:
                    if inst.opname == 'LOAD_METHOD' and inst.argval in self.prohibited_methods:
                        raise TypeError(
                            f'Forbidden call detected: {inst.argval}'
                        )
                    if inst.argval in self._TCP:
                        self._TCP[inst.argval] = True

        if False in self._TCP.values():
            raise TypeError('The socket is not using TCP')

        super().__init__(clsname, bases, clsdict)
