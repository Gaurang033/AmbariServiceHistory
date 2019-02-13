const defaultState = {
    service_status : {},
    toolTipOpen: false,
    inteval: 1 // in minutes
}

const mainReducer = (state=defaultState, action) => {
    switch(action.type){
        default:
        return state

        case 'FETCH_SERVICE_STATUS': 
        return {
            ...state,
            service_status: action.data
        }

        case 'TOOGLE_TOOLTIP':
        return {
            ...state,
            toolTipOpen: action.id
        }

    }
}

export default mainReducer