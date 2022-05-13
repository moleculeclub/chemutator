from chemutator.evo_utils import (
    get_list_link_idxs,
    # get_link_idx,
)


def test_get_list_link_idxs():
    smi = 'CC(C(=O)O)c1ccc2oc(-c3ccc(Cl)cc3)nc2c1'
    assert get_list_link_idxs(smi) == [4, 6, 7, 12, 13, 16, 17, 20]

    smi = 'C=C(CC)C(=O)c1ccc(OCC(=O)O)c(Cl)c1Cl'
    assert get_list_link_idxs(smi, True) == [0, 2, 3, 7, 8, 11, 14]

    smi = 'CN1CC2CC3=CC(C(=O)CC3)C3C=C(CCC3=O)CC1CN2'
    assert get_list_link_idxs(smi) == [22]
