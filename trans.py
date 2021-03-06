# http://rosalind.info/problems/tran/

def problem(s1, s2):
    transitions = set([('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')])
    ratio = {True: 0.0, False: 0.0}
    for p in zip(s1, s2):
        if p[0] != p[1]:
            ratio[p in transitions] += 1
    return ratio[True] / ratio[False]


if __name__ == '__main__':
    print problem("AGAACGTATGTCATAACTACTTAAACACTGCTTTTTTATCTGATGGGTCCGTATGGCTGCGAGGGGTCCGTGTGGTCAGTATCCGTCATCCCTTTATCACACGATATGAGGAACTAACGAGCTAATAGGTTGACCTCGCGGGAGCAAACGTATAGTCAGTCTTATCTGGAGATTCTCATTCGAACAATAGTACAGGCGATGATAGGTAGTTGACCGCGAGTCCGTCCTTATAGATCCATCGTACGCTGTCTTAATGGTCGTATCCCTTTGCTGGCCCATCCGCCTAGGCTACGTTACTTCAAGTCGCTCCAATGCTAACTGTCGACGGGTCGTCAAGTCAATTTCGGATTGGCGCGAATATGAAGTTTCCGGAAAACAGGCAGACATGGCCGGAGTGTGTTCTAGGCGGAGGGTGTCCCCACCGTTGGTCAAGCTATAGGTCTCTCGACCACACGATCGCGGCTCTAACAGGCTTTTTTCCGCACTCTACCTATCGTGCCGGCGTCTTCTTCAGTCGGCAAGTCTCATCGACGACAATACAATCGCGTATACCAGACGTGCTCACTGTATCAAATAGGGTTATAATCTACATGGGCGTCCGTAACACAATGCTGGTGTGCCGTGATTTAGTGTTAGGCATAGCGAAGTCCCGTGACATGAACAATTGAACGACCCGACGGGTCGCCCTCAAAGGAATGGATGGGCTTATACTAGTCGCGAAACGTTGGCACGAACCGCTGATTGTGCGGGTGTGTATCACTACTAGCGGCCCGCAGAGTCTAAGACGCCCTCAGAACAAAGATACTAACGAGC", 
                  "GGAGGTTATGCCCTAACTCCCTAAATACCGCTCTACCATCTAACAGGTCAGCATGGCTGCTGAGGGTGCGTGTGCTCAATATCGGTCATCCGCTTATCATATGGTACGAGGAACTAAGGAATTGACAAGCTGACCACGCGGGAGCAACCGTATGGTCAATCGTGTGTGCAGACCATCATTCCGACAATATTATAGCTAATAGCGAATAGTTTACCACGGGTCTGTCCATATAAATCTAGCGTACGCTGTCTTAATGGTCCTAGCCTTCCCATGGCCCATCAGCCTGAGCTACGTCAGTTCAAGTTGCTCCAACGCCAACCGCCGACGGATCGCTGAGTCGATGCTGGACTGACGCGGATGAAAGACTTCCAAGGAGCGGGCGACCAGGCTCGGAGTGTGTTATGGGCATAAGCTACTCCCACCGTTAATAAAGCTATGCGGCATTGTACTACAAGGTCGCAACTCCGGCGGGGTCTTTCCCGTACTATACTTGTCGCGCCGATTCCCTGTTTAGCTGACGACTCCCGTTGACGACAACATAATCACGTATGCCAAACGCTCCCACTGCATTAAATAAATTTTTAACCAACATGGGTGTCCGTAACACAGTGCCGCCTTCTTGTGATTTAGTGTTGGACATAGCGAAACATCGCGATATGAACAGGTGAGCGGTCCGGAGGGACACCTTTAAGGGAATGGACGGGCTCACACTGGCCGCAGTGTATGAGCCCGAACTGCTGGTTAGGCGGGTGTGTATCACCGCTAGCAGCTCGCAGGATCTAGAACGCTCTCGGAACTAAGACACTGTCGAGC")
