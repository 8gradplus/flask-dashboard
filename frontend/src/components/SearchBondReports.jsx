import {useEffect, useRef, useState} from "react";
import {TextField} from "@mui/material";

export function SearchBondReports({onSearchResultClick}) {
    const [searchText, setSearchText] = useState('')
    const [candidates, setCandidates] = useState([])
    const loading = useRef(false)
    useEffect(() => {
        // checking for data is not sufficient, because loading
        // may be in progress, but not yet finished
        if (loading.current) return
        loading.current = true
        fetch('api/search')
            .then((resp) => resp.json())
            .then(setCandidates)
    }, [])

    let handleSearchTextChange = (e) => {
        setSearchText(e.target.value.toLowerCase())
    }

    let handleSearchResultClick = (e) => {
        onSearchResultClick(e)
        // Reset Search Results
        setSearchText('')

    }
    return (
        <div>
            <SearchBar
                value={searchText}
                onChange={handleSearchTextChange}
            />
            <SearchTable
                candidates={candidates}
                searchText={searchText}
                onClick={handleSearchResultClick}
            />
        </div>
    )
}

function SearchBar({value, onChange}) {
    return (
        <TextField
            id="bondReportSearchBar"
            label="Isin / Bond name"
            type="search"
            variant="outlined"
            value={value}
            onChange={onChange}
        />

    )
}

function SearchTable({candidates, searchText, onClick}) {
    // todo: use mui table
    const search_result = []

    candidates.forEach((candidate) => {
            // todo add bondNome
            if(searchText === ''){
                return;
            }
            if (candidate.isin.toLowerCase().indexOf(searchText) === -1 &&
                candidate.bondName.toLowerCase().indexOf(searchText) === -1
            ) {
                return;
            }
            search_result.push(<SearchRow candidate={candidate}
                                          onClick={onClick}
                                          key={candidate.isin}/>)
        }
    )
    if (search_result.length !== 0) {return (
        <table>
            <thead>
            <tr>
                <th>Isin</th>
                <th>Bond Name</th>
                <th>Issue Date</th>
            </tr>
            </thead>
            <tbody>{search_result}</tbody>

        </table>
    )};
}

function SearchRow({candidate, onClick}) {
    return (
        <tr
            onClick={() => onClick(candidate.isin)}>
            <td>{candidate.isin}</td>
            <td>{candidate.bondName}</td>
            <td>{candidate.issueDate}</td>
        </tr>
    )

}