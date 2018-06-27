
def route(moves):
  u,d,l,r = map(moves.count, 'UDLR')
  return u == d and l == r
