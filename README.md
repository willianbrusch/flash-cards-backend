# Projeto Flash Cards Review

## Objetivo

Criar uma aplicação que permita cadastrar usuários. Eles devem poder criar decks com diferentes cards. Além disso será implementado um algoritmo para revisão espaçada.

## Tecnologias Utilizadas

- Python
- Django
- Django Rest Framework
- Pytest
- Postgresql

## Entidades Planejadas

### User (Usuário)

- id
- name
- email
- password
- created_at
- updated_at

#### Deck (Conjunto de Flashcards)

- id
- title
- description
- user_id (Relacionamento com o usuário criador)
- created_at
- updated_at

### Card (Flashcard)

- id
- deck_id (Relacionamento com o deck)
- question
- answer
- created_at
- updated_at

### Review (Controle de Revisões por Card)

- id
- card_id (Relacionamento com o card)
- user_id (Relacionamento com o usuário)
- easiness_factor (EF — fator de facilidade)
- interval (Intervalo até a próxima revisão)
- repetitions (Número de acertos consecutivos)
- last_reviewed_at (Última revisão)
- next_review_at (Próxima revisão)
- score (Nota da última revisão — 0 a 5)
- created_at
- updated_at

Obs. Implementar projeto base e depois trocar ambiente de desenvolvimento para dynaconf
