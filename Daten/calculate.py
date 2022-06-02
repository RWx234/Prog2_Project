def max_bak_berechnen(vol_alk, p_alk, m_person, gender, age):
    m_eth = vol_alk * (p_alk/100) * 0.8
    if age < 18 or gender == "female":
        bak = m_eth / (m_person * 0.55)
    elif gender == "male":
        bak = m_eth / (m_person * 0.68)
    elif gender == "other":
        bak = m_eth / (m_person * ((0.68+0.55)/2))
    # min resorptionsfaktor 10%
    max_bak = bak * 0.9
    return max_bak


def min_bak_berechnen(vol_alk, p_alk, m_person, gender, age):
    m_eth = vol_alk * (p_alk/100) * 0.8
    if age < 18 or gender == "female":
        bak = m_eth / (m_person * 0.6)
    elif gender == "male":
        bak = m_eth / (m_person * 0.7)
    elif gender == "other":
        bak = m_eth / (m_person * ((0.6+0.7)/2))
    # max resorptionsfaktor 30%
    min_bak = bak * 0.7
    return min_bak

