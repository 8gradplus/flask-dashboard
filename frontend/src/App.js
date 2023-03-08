import {SearchBondReports} from "./components/SearchBondReports";
import {useState} from "react";


function App() {
    //fetch('api/search').then((r) => r.json()). then((r) => console.log(r))
    const [isin, setIsin] = useState(undefined)

    return (
        <div className="app">
            {/*<Navbar/> */}
            <h2>{isin}</h2>
            <SearchBondReports onSearchResultClick={setIsin}/>



        </div>
    );
}

export default App;
