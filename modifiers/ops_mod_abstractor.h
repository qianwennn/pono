/*********************                                                  */
/*! \file ops_mod_abstractor.h
** \verbatim
** Top contributors (to current version):
**   
** This file is part of the pono project.
** Copyright (c) 2019 by the authors listed in the file AUTHORS
** in the top-level source directory) and their institutional affiliations.
** All rights reserved.  See the file LICENSE in the top-level source
** directory for licensing information.\endverbatim
**
** \brief Abstract arrays using uninterpreted functions.
**
**
**/

#pragma once

#include "smt-switch/identity_walker.h"

#include "abstractor.h"

namespace pono {

smt::Term abstract_op(const smt::Term & in, const smt::SmtSolver & solver_);


} // namespace pono
