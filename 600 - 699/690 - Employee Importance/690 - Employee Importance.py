class Solution:
    def getImportance(
            self,
            employees: List['Employee'],
            id: int) -> int:  # 44.64% 9.91%
        total = 0
        target = [id]
        map_e = {emp.id: emp for emp in employees}
        while target:
            cur = map_e[target.pop()]
            if cur.subordinates:
                target.extend(cur.subordinates)
            total += cur.importance
        return total

    def getImportance_same_speed_map(
            self,
            employees: List['Employee'],
            id: int) -> int:
        employee = {e.id: e for e in employees}
        def calc_imp(id):
            e = employee[id]
            return e.importance+sum(map(calc_imp, e.subordinates))
        return calc_imp(id)

    def getImportance_initial(
            self,
            employees: List['Employee'],
            id: int) -> int:  # 84.68% 37.60%
        map_e = {emp.id: emp for emp in employees}
        total = map_e[id].importance
        target = map_e[id].subordinates
        while target:
            cur = map_e[target.pop()]
            if cur.subordinates:
                target += cur.subordinates
            total += cur.importance
        return total

    def getImportance_best_speed(self, employees: List['Employee'], id: int) -> int:
        employees_lookup = dict()
        for employee in employees:
            employees_lookup[employee.id] = employee
        total_importance = employees_lookup[id].importance
        target_employee_subordinates = employees_lookup[id].subordinates
        while target_employee_subordinates:
            subordinate_employee_id = target_employee_subordinates.pop(0)
            total_importance = (
                total_importance +
                employees_lookup[subordinate_employee_id].importance
            )
            if employees_lookup[subordinate_employee_id].subordinates:
                target_employee_subordinates += (
                    employees_lookup[subordinate_employee_id].subordinates
                )
        return total_importance

    def getImportance_best_memory(
            self,
            employees: List['Employee'],
            id: int) -> int:
        n = len(employees)
        need = set()
        need.add(id)
        sm = 0
        while need:
            for i in range(n):
                if employees[i].id in need:
                    sm += employees[i].importance
                    need.remove(employees[i].id)
                    for sub in employees[i].subordinates:
                        need.add(sub)
        return sm
