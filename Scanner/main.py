from domain.SymbolTable import SymbolTable
from domain.PIF import PIF

st = SymbolTable()
print(st.put('abc'))
print(st.put('abcd'))
print(st.put('abc'))
print(st.put(12))
print(st.put('_abc14'))
print(st.put(12))
print(st.put(13))

PIF = PIF(st)

PIF.genPIF('+')
PIF.genPIF('var')
PIF.genPIF('if')
PIF.genPIF('const')
PIF.genPIF('abc')
PIF.genPIF(12)
print('PIF:')
PIF.print()






