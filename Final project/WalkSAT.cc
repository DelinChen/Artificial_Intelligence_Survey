#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <cmath>
#include <ctime>
#include "Clause.h"

class Walksat {
	std::vector<Clause> clauses;
	std::unordered_map<int, bool> model;
	Clause ranclause;
	constexpr static float PROB = 0.5;
	const int MAX_FLIPS = std::pow(10, 5);

public:
	Walksat(std::string);
	int algorithm();

private:
	inline bool sat();
	inline void flipmax();
	void getclauses(std::string);
};

inline bool Walksat::sat() {
	for(Clause c : clauses) {
		if(!c.satisfies(model))
			return false;
	}
	return true;
}

inline void Walksat::flipmax() {
	int satcount = 0, flipsymbol;
	std::vector<int> symbols = ranclause.clauses();
	bool flipbool;

	for (int i = 0; i < symbols.size(); i++) {
		flipbool = model[symbols[i]];
		model[symbols[i]] = !flipbool;
		int testcount = 0;

		for(Clause c : clauses) {
			if(c.satisfies(model))
				testcount++;
		}

		if(satcount<testcount) {
			satcount = testcount;
			flipsymbol = symbols[i];
		}

		model[symbols[i]] = flipbool;
		testcount = 0;
	}
	model[flipsymbol] = !model[flipsymbol];
}


void Walksat::getclauses(std::string filename) {
	std::string line;
	std::ifstream f(filename);

	if (!f.is_open()) {
		std::cout << "Error opening file" << std::endl;
		exit(0);
	}

	std::cout << "Prob: " << PROB << " Max Flips: " << MAX_FLIPS << std::endl;

	getline(f, line);
	std::cout << line << std::endl;

	while (getline(f, line)) {
		Clause c = Clause(line);
		clauses.push_back(c);
	}

	f.close();
}

Walksat::Walksat(std::string filename) : ranclause("1 1 1") {	
	getclauses(filename);
	std::srand(time(NULL));
	for (Clause c : clauses) {
		for (int s : c.clauses()) {
			if (model.count(s) == 0) 
				model[s] = std::rand() % 2;
		}
	}
}

int Walksat::algorithm() {
	for (int currentFlips = 0; currentFlips < MAX_FLIPS; currentFlips++) {
		std::cout << "\rCurrent flips: " << currentFlips;

		if(sat()) {
			std::cout << '\r';
			return currentFlips;
		}
		while (true) {
		ranclause = clauses[std::rand() % (clauses.size())];
		if (!ranclause.satisfies(model))
			break;
		}

		if(std::rand() / double(RAND_MAX) < PROB)
			model[ranclause.randomClause()] = !model[ranclause.randomClause()];
		else
			flipmax();
	}
	return -1;
}

int main (int argc, char* argv[]) {
	if (argc != 2) {
		std::cout << "input cnf file required" << std::endl;
		exit(0);
	}

	Walksat walksat = Walksat(argv[1]);
	clock_t START_TIMER = clock();
	int result = walksat.algorithm();
	std::cout
        << "Elapsed time: "
        << (clock() - START_TIMER) / (double)CLOCKS_PER_SEC << "s"
        << std::endl;
	if (result == -1)
		std::cout << "\r"
			 << "\rFailure" << std::endl;
	else
		std::cout << "\rWalkSat flips: " << result << std::endl;
}	