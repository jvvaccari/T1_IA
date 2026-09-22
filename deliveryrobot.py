class DeliveryRobotState:
    """
    Representa o estado do problema do robô de entrega.
    Guarda a localização atual e o nível de bateria.
    """
    def __init__(self, location, battery):
        self.location = location
        self.battery = battery

    def __eq__(self, other):
        """
        Permite que o Python compare dois estados para checar se são idênticos.
        Crucial para o conjunto `expanded` (ou `visited`) não entrar em loop.
        """
        if not isinstance(other, DeliveryRobotState): 
            return False
        return self.location == other.location and self.battery == other.battery

    def __hash__(self):
        """
        Permite que este estado seja inserido em um 'set' ou usado como chave de dicionário.
        """
        return hash((self.location, self.battery))

    def __str__(self):
        """
        Formatação amigável para printar os estados no console.
        """
        return f"(Local: {self.location}, Bateria: {self.battery})"


class DeliveryRobotSearchProblem:
    """
    Esta classe define o mapa, as regras e a dinâmica de transição do problema.
    """
    def __init__(self):
        # Representação do grafo (as conexões bidirecionais)
        self.graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'D'],
            'D': ['B', 'C', 'E'],
            'E': ['D']
        }
        self.max_battery = 3
        self.recharge_station = 'C'
        self.goal_location = 'E'
        
        # Estado Inicial: Local A, Bateria 2
        self.start_state = DeliveryRobotState('A', 2)

    def getStartState(self):
        """
        Retorna o estado inicial.
        """
        return self.start_state

    def isGoalState(self, state):
        """
        Verifica se o robô chegou no destino final, independente da bateria.
        """
        return state.location == self.goal_location

    def expand(self, state):
        """
        Gera os nós filhos retornando uma lista de tuplas: (nextState, action, stepCost)
        """
        successors = []
        loc = state.location
        bat = state.battery

        # 1. Ação de Movimento: Só pode mover se tiver bateria
        if bat > 0:
            for neighbor in self.graph[loc]:
                next_state = DeliveryRobotState(neighbor, bat - 1)
                action = f"{loc}->{neighbor}"
                cost = 1
                successors.append((next_state, action, cost))

        # 2. Ação de Recarga: Só ocorre no posto C e se a bateria não estiver cheia
        if loc == self.recharge_station and bat < self.max_battery:
            next_state = DeliveryRobotState(loc, self.max_battery)
            action = "RECARREGAR"
            cost = 1
            successors.append((next_state, action, cost))

        return successors

    def getSuccessors(self, state):
        """ 
        Alias (apelido) para expandir, caso seu algoritmo chame getSuccessors.
        """
        return self.expand(state)

if __name__ == '__main__':
    import search

    problem = DeliveryRobotSearchProblem()
    state = problem.getStartState()
    actions = search.breadthFirstSearch(problem)

    print("Estado inicial:", state)
    print("Ações encontradas pelo BFS:", actions)
    print("Sequência de estados e ações:")

    total_cost = 0
    print(f"  {state}")
    for action in actions:
        for next_state, next_action, step_cost in problem.expand(state):
            if next_action == action:
                total_cost += step_cost
                print(f"  -- {action} (custo {step_cost}) --> {next_state}")
                state = next_state
                break
        else:
            raise ValueError(f"Ação ilegal na solução: {action}")

    print("Estado final:", state)
    print("Custo total:", total_cost)