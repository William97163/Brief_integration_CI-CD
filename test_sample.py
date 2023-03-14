"""
Les fonctions à tester sont les méthodes 'encrypt' et 'decrypt'
des classes contenues dans les fichiers dont le nom se termine
par 'algo.py'. À noter que certaines classes n'ont pas de méthode
decrypt, ou uniquement une méthode vide.

Pour savoir quelles sont les entrées et/ou le format des clés attendus
par ces différentes fonctions de cryptage/décryptage, vous pouvez lancer 
l'application et lire les encadrés d'information à droite, et faire des 
recherches.

Pour lancer tous les tests contenus dans ce fichier, utilisez 
la commande pytest <nom de ce script>
"""


# import des class
from crypto_app.aes_algo import AdvancedEncryptionStandard
from crypto_app.blowfish_algo import Blowfish
from crypto_app.caesarcipher_algo import CaesarCipher
from crypto_app.des_algo import DES
from crypto_app.enigmam3_algo import EnigmaM3
from crypto_app.md5_algo import MD5
from crypto_app.sha_algo import SHA
from crypto_app.vigenerecipher_algo import VigenereCipher



def test_enigma():
    """
    Un exemple de fonction de test, ici avec le cryptage
    d'Enigma.
    """

    enigma = EnigmaM3()
    msg = "Message"
    key = [
        ('A', 'C', 'N'),
        (2, 4, 1),
        ('F', 'H', 'K'),
        [('A', 'K')]
    ]

    encrypted = enigma.encrypt(msg, key)
    assert encrypted == "FUTALDK"
    decrypted = enigma.decrypt(encrypted, key)
    assert decrypted == "MESSAGE"



#######################################################
# AJOUTEZ VOS TESTS À LA SUITE
#######################################################


def test_aes():
    
    aes = AdvancedEncryptionStandard()
    msg = "Message"
    key = '16 caracteres !!'
    encrypted = aes.encrypt(msg, key)
    assert encrypted == "5e10b9901384af"
    decrypted = aes.decrypt(encrypted, key)
    assert decrypted == "Message"
    

def test_blowfish():
    
    blow = Blowfish()
    msg = "Message"
    key = 'bbbb'
    encrypted = blow.encrypt(msg, key)
    decrypted = blow.decrypt(encrypted, key)
    assert decrypted == "Message"
    
def test_CaesarCipher():
    
    cipher = CaesarCipher()
    msg = "msg"
    key = 1
    encrypted = cipher.encrypt(msg, key)
    assert encrypted == "nth"
    decrypted = cipher.decrypt(encrypted, key)
    assert decrypted == "msg"
    

def test_DES():
    
    des = DES()
    msg = "message"
    key = "16 caracteres !!"
    encrypted = des.encrypt(msg, key)
    assert encrypted == "c746f006ae2af1b3"
    

def test_MD5():
    
    md5 = MD5()
    msg = "message"
    encrypted = md5.encrypt(msg)
    assert encrypted == "78e731027d8fd50ed642340b7c9a63b3"
    

def test_SHA():
    
    sha = SHA()
    msg = "message"
    encrypted = sha.encrypt(msg)
    assert encrypted == "f8daf57a3347cc4d6b9d575b31fe6077e2cb487f60a96233c08cb479dbf31538cc915ec6d48bdbaa96ddc1a16db4f4f96f37276cfcb3510b8246241770d5952c"
    
def test_VigenereCipher():
    
    vig = VigenereCipher()
    msg = "message"
    key = 'abcd'
    encrypted = vig.encrypt(msg, key)
    assert encrypted == 'mfuvahg'

    