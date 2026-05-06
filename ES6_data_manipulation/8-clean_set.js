const cleanSet = (set, startString) => {
	if (!startString || typeof startString !== 'string') return '';
	return Array.from(set)
		.filter((x) => x.startsWith(startString))
		.map((x) => x.slice(startString.length))
		.join('-')
}
export default cleanSet
