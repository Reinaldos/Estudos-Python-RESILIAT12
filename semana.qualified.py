def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
  global podio
  if tempo_chegada1 < tempo_chegada2 and tempo_chegada1 < tempo_chegada3:
    podio = (f'1 - {tempo_chegada1} minutos\n2 - {tempo_chegada2} minutos\n3 - {tempo_chegada3} minutos\n')
    
  if tempo_chegada1 < tempo_chegada3 and tempo_chegada3 < tempo_chegada2:
    podio = (f'1 - {tempo_chegada1} minutos\n2 - {tempo_chegada3} minutos\n3 - {tempo_chegada2} minutos\n')

  if tempo_chegada2 < tempo_chegada1 and tempo_chegada2 < tempo_chegada3:
    podio = (f'1 - {tempo_chegada2} minutos\n2 - {tempo_chegada1} minutos\n3 - {tempo_chegada3} minutos\n')
  
  if tempo_chegada2 < tempo_chegada3 and tempo_chegada3 < tempo_chegada1:
    podio = (f'1 - {tempo_chegada2} minutos\n2 - {tempo_chegada3} minutos\n3 - {tempo_chegada1} minutos\n')

  if tempo_chegada3 < tempo_chegada1 and tempo_chegada3 < tempo_chegada2:
    podio = (f'1 - {tempo_chegada3} minutos\n2 - {tempo_chegada1} minutos\n3 - {tempo_chegada2} minutos\n')
    
  if tempo_chegada3 < tempo_chegada2 and tempo_chegada2 < tempo_chegada1:
    podio = (f'1 - {tempo_chegada3} minutos\n2 - {tempo_chegada2} minutos\n3 - {tempo_chegada1} minutos\n')
  
    
  return str(f'{podio}')