"""Programme principal pour tester la fonction ispalindrome."""
import unicodedata
def normaliser(s: str) -> str:
    """Supprime les accents et caractères spéciaux d'une chaîne Unicode,
    remplace les ligatures, et ne garde que lettres et chiffres.
    """
    s = unicodedata.normalize('NFKD', s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.lower()
    s = "".join(c for c in s if c.isalnum())

    return s

def ispalindrome(p: str) -> bool:
    """Renvoie True si la chaîne p est un palindrome, False sinon."""
    p = normaliser(p)
    return p == p[::-1]



def main() -> None:
    """appel main pour tester la fonction ispalindrome."""

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
