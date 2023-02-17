export function useGetter(getterString) {
    const data = localStorage.getItem(getterString)

    if (typeof(data) === 'undefined' || data === null ) {
        return []
    }
    return Array.from(JSON.parse(localStorage.getItem(getterString)))

}

export function useSetter(item, setterString, number) {
    const recentData = localStorage.getItem(setterString)

    if(recentData === null || typeof(recentData) === 'undefined') {
      const data = [item]
      localStorage.setItem(setterString, JSON.stringify(data))
      return true
    }

    const getCurrentData = Array.from(JSON.parse(recentData))
    if (getCurrentData.length < number) {
         const isItemExist = getCurrentData.filter(data => String(data?.title) === String(item?.title))

         if (isItemExist.length === 0) {
             let new_items = [...getCurrentData, item]
             localStorage.setItem(setterString, JSON.stringify(new_items))
             return true
         }
    }
    else{
        let editData = [...getCurrentData]
        editData.pop(0)
        editData.push(item)
        localStorage.setItem(setterString, JSON.stringify(editData))
        return true
    }

    return false

}

export function deleteSetter(item, setterString) {
     // method to delete particular recent
     const getData =  Array.from(JSON.parse(localStorage.getItem(setterString)))
     const recents = getData.filter(data => String(data?.title) !== String(item?.title))
     localStorage.setItem(setterString, JSON.stringify(recents))
     return
}