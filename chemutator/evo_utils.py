from rdkit import Chem  # type: ignore
from random import choice
from typing import List


def get_list_link_idxs(
    smi: str,
    include_non_aro_carbon: bool = False,
) -> List[int]:
    """
    Returns a list of atoms that can be linked to another molecule. Contains
    all OH and NH and only aromatic CH. If include_non_aro_carbon == True, all
    CH will be included.

    Examples
    --------
    >>> get_list_link_idxs('CN1CC2CC3=CC(C(=O)CC3)C3C=C(CCC3=O)CC1CN2')
    [7, 8, 14]

    Parameters
    ----------
    smi: str
        The input SMILES string.
    include_non_aro_carbon: bool
        Flag to include non-aromatic carbons.

    Returns
    -------
    List[int]
        List of atom indices that can be linked to another molecule.
    """
    mol = Chem.MolFromSmiles(smi)
    link_idxs = []
    for i, atom in enumerate(mol.GetAtoms()):
        if atom.GetTotalNumHs() > 0:
            if (atom.GetSymbol() == 'N' or
               atom.GetSymbol() == 'O'):
                link_idxs.append(i)
            elif (atom.GetSymbol() == 'C' and (include_non_aro_carbon or
                  atom.GetIsAromatic())):
                link_idxs.append(i)
    return link_idxs


def get_link_idx(
    smi: str,
    include_non_aro_carbon: bool = False,
) -> int:
    """
    Returns a single atom that can be linked to another molecule. Will be an
    NH, OH, or aromatic CH. If include_non_aro_carbon == True, it can be any
    CH.

    Examples
    --------
    >>> get_link_idx('CN1CC2CC3=CC(C(=O)CC3)C3C=C(CCC3=O)CC1CN2')
    8

    Parameters
    ----------
    smi: str
        The input SMILES string.
    include_non_aro_carbon: bool
        Flag to include non-aromatic carbons.

    Returns
    -------
    int
        An atom index that can be linked to another molecule.
    """
    link_idxs = get_list_link_idxs(smi, include_non_aro_carbon)
    return choice(link_idxs)



