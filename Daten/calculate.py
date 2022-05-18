def bak_berechnen(vol_alk, p_alk, m_person, gender, age):
    # Resorptionsfaktor noch einbauen (10 - 30 Prozent)
    m_eth = vol_alk * (p_alk/100) * 0.8
    if age < 18 or gender == "female":
        bak = m_eth / (m_person * 0.575)
    elif gender == "male":
        bak = m_eth / (m_person * 0.69)
    elif gender == "other":
        bak = m_eth / (m_person * ((0.69+0.575)/2))
    return bak

