from ._base import Descriptor
from ._common import Eccentricity, Valence


class EccentricConnectivityIndex(Descriptor):
    r'''
    eccentric connectivity index descriptor

    .. math::
        I_{\rm EC} = \sum^A_i {\boldsymbol E}{\boldsymbol V}

    where
    :math:`E` is eccentricity of atoms,
    :math:`V` is valences of atoms.

    :rtype: int
    '''

    explicit_hydrogens = False
    require_connected = False

    def __str__(self):
        return 'ECIndex'

    def dependencies(self):
        return dict(
            E=Eccentricity(
                self.explicit_hydrogens,
                False,
                False,
            ),
            V=Valence(
                self.explicit_hydrogens,
                False,
            ),
        )

    def calculate(self, mol, E, V):
        return (E.astype('int') * V).sum()
