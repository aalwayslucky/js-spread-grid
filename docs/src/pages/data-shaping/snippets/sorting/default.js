function render(sortBy) {
    SpreadGrid(div, {
        data: [
            // collapse: true
            // default data
            // collapse: false
        ],
        // collapse: true
        columns: [{ type: 'DATA-BLOCK', width: 70 }],
        // collapse: false
        sortBy: sortBy,
        onSortByChange: render
    });
}

render([{ columnId: "age", direction: "ASC" }]);