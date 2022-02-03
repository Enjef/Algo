class Solution:
    def peopleIndexes(self, favoriteCompanies) -> List[int]:  # 56.25% 75.00%%
        count = {}
        out = []
        for i in range(len(favoriteCompanies)):
            count[i] = set(favoriteCompanies[i])
        for i in range(len(favoriteCompanies)):
            cur = count[i]
            for key in count:
                if key != i and cur.issubset(count[key]):
                    break
            else:
                out.append(i)
        return out

    def peopleIndexes_best_speed(self, favoriteCompanies) -> List[int]:
        favoriteCompanySets = []
        favoriteCompanyLenByInd = defaultdict(list)
        maxLength = 0
        for i, compList in enumerate(favoriteCompanies): 
            length = len(compList)
            favoriteCompanySets.append(set(compList))
            favoriteCompanyLenByInd[length].append(i)
            if length > maxLength:
                maxLength = length

        def isNotSubsetOfLargerCompanies(companyIndex):
            nonlocal maxLength
            companySet = favoriteCompanySets[companyIndex]
            for length in range(len(companySet)+1, maxLength+1):
                largerCompanies = favoriteCompanyLenByInd[length]
                for largerIndex in largerCompanies:
                    if companySet.issubset(favoriteCompanySets[largerIndex]):
                        return False
            return True
        
        return list(
            filter(isNotSubsetOfLargerCompanies,
            range(len(favoriteCompanies)))
        )

    def peopleIndexes_2nd_best_speed(self, favoriteCompanies: List[List[str]]):
        largest_subsets = []
        non_subset_idx = []
        remove_idx = set()
        for i,fav_comp  in enumerate(favoriteCompanies):
            curr_set = set(fav_comp)
            present = False
            for j,test_set in zip(non_subset_idx,largest_subsets):
                if curr_set <= test_set:
                    present = True
                    break
                elif test_set < curr_set:
                    remove_idx.add(j)       
            if not present:
                largest_subsets.append(curr_set)
                non_subset_idx.append(i)
        return sorted(list(set(non_subset_idx) - remove_idx))

    def peopleIndexes_best_memory(self, favoriteCompanies):
        values = dict()
        for index, companies in enumerate(favoriteCompanies):
        set_vals = set(companies)
        superset_of = [i for i, j in values.items() if set_vals.issuperset(j)]
        if not any(set_vals.issubset(j) for i, j in values.items()):
            values[index] = set_vals
        if len(superset_of) > 0:
            for sup_idx in superset_of:
            del values[sup_idx]
        return sorted(values.keys())
