class Person:
    def __init__(self, name, born=None, died=None, mom=None, dad=None):
        self.name = name
        self.born = born
        self.died = died
        self.mom = mom
        self.dad = dad

    def is_sibling_of(self, other): #the reason we say self its because i'ts within the class
        same_mom = self.mom is not None and other.mom is not None and self.mom is other.mom
        same_dad = self.dad is not None and other.dad is not None and self.dad is other.dad
        # Half or full, we don't care
        return same_mom or same_dad  #you have a brother or sister if you have the same mom or dad so u write exactly that
    
    def is_parent_of(self, other):
        """Return if this person is a parent of the other person."""
        return other is not None and (other.mom is self or other.dad is self)

    def is_child_of(self, other):
        """Return if this person is a child of the other person."""
        return other.is_parent_of(self)

    def is_grandparent_of(self, other):
        """Return if this person is a grandparent of another person."""
        return other is not None and (
            (other.mom is not None and self.is_parent_of(other.mom)) or
            (other.dad is not None and self.is_parent_of(other.dad)))
    
    def print_family_tree(self, prefix="", level=0):
        """Print the family tree starting from this person."""
        indent = "    " * level
        print(f"{prefix}{self.name} {self.born or '?'}-{self.died or '?'}")
        if self.mom:
            self.mom.print_family_tree(f"  {indent}mom: ", level + 1)
        if self.dad:
            self.dad.print_family_tree(f"  {indent}dad: ", level + 1)

    def __str__(self):
        span = f"({self.born or '?'}-{self.died or '?'})"
        mom = f"{self.mom.name if self.mom is not None else '?'}"
        dad = f"{self.dad.name if self.dad is not None else '?'}"
        return f"{self.name} {span} mom: {mom}, dad: {dad}"

odi = Person("Odelie Copele", born="1824", died="1873")
paul = Person("Paul Grambois", born="1806")
eugenie = Person("Eugénie Granbois", born="1838", died="1907", mom=odi, dad=paul)
celeste = Person("Céleste Lamelle", born="1814", died="1877")
joey_b = Person("Joey Baquié", born="1811", died="1882")
ferdinand = Person("Ferdinand Baquié", born="1837", died="1883", mom=celeste, dad=joey_b)
louise = Person("Louise Baquié", born="1868", died="1945", mom=eugenie, dad=ferdinand)
julie = Person("Julienne Montreuil", born="1796", died="1833")
agenor = Person("Agenor Ramos", born="1803", died="1846")
marie = Person("Marie Ramos", born="1826", died="1904", mom=julie, dad=agenor)
marge = Person("Marguerite Cadeneth", born="1804", died="1870")
giacamo = Person("Giacamo Martino", born="1806", died="1852")
jacques = Person("Jacques Martinez", born="1822", died="1891", mom=marge, dad=giacamo)
joseph = Person("Joseph Martinez", born="1864", died="1926", mom=marie, dad=jacques)
mildred = Person("Mildred Martinez", born="1911", died="1990", mom=louise, dad=joseph)
jeanne_c = Person("Jeanne Chauvin", born="1840", died="1866")
romain = Person("Romain Prévost", born="1832", died="1879")
jeanne_p = Person("Jeanne Prévost", born="1864", mom=jeanne_c, dad=romain)
louise_a = Person("Louise Aubin", born="1814", died="1909")
pierre = Person("Pierre Fontaine", born="1818", died="1886")
ernie = Person("Ernest Fontaine", born="1857", died="1919", mom=louise_a, dad=pierre)
suzanne = Person("Suzanne Fontaine", born="1894", died="1979", mom=jeanne_p, dad=ernie)
vittoria = Person("Vittoria Trusiano", born="1813", died="1880")
francesco = Person("Francesco Alioto", born="c1813", died="c1880")
maria = Person("Maria Alioto", born="1834", died=">1908", mom=vittoria, dad=francesco)
concetta = Person("Concetta Buccafusca", born="c1795", died="1843")
giuseppe = Person("Giuseppe Riggitano", born="c1786", died="1864")
santo = Person("Santo Riggitano", born="1824", died="c1898", mom=concetta, dad=giuseppe)
salvatore = Person("Salvatore Riggitano", born="1876", died="1960", mom=maria, dad=santo)
louis = Person("Louis Prevost", born="1920", died="1997", mom=suzanne, dad=salvatore)
leo = Person("Robert Prevost", born="1955", mom=mildred, dad=louis)
adele = Person("Adele Martinez", mom=marie, dad=jacques)

print(adele.is_sibling_of(joseph)) # should be true
print(joseph.is_sibling_of(adele)) # should be true
print(salvatore.is_sibling_of(louise)) # should be false
print(santo.is_child_of(giuseppe)) # should be true
print(leo.is_child_of(louis)) # should be false

leo.print_family_tree() # Person.print_family_tree()is the structure also u put the "." cuz it's a method

#function inside a class is called a method 
#function outside a class is just a function
#va aponer en el examen lo de is_sibling_of 
# "is" checks identity and the = checks the value 
# a=b this means that whatever is in the b box will now be in the a box and after that if we write a is b wil now be true 
# F is important when doing def __str(self): return f"(...)
