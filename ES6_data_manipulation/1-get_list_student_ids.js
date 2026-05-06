const getListStudentIds = (getListStudents) => {
	if (!Array.isArray(getListStudents)){
		return[];
	}
	else {
		return getListStudents.map((student) => student.id);
	}
}

export default getListStudentIds