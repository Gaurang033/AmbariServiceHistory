import axios from 'axios'

export function getServiceStatus() {
    return function(dispatch){
        axios.get("http://localhost:5005/api/all_services")
        .then(response => {
            return dispatch(getServiceStatusAction(response.data))
        }).catch(response => {
        }
            
        )
    }
}

export function getServiceStatusAction(data) {
    return {
        type: 'FETCH_SERVICE_STATUS', 
        data: data
    }
}


export function toogleToolTipAction(id) {
    return {
        type: 'TOOGLE_TOOLTIP',
        id
    }
}