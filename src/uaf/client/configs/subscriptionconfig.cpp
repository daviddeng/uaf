/* This file is part of the UAF (Unified Architecture Framework) project.
 *
 * Copyright (C) 2012 Wim Pessemier (Institute of Astronomy, KULeuven)
 *
 * Project website: http://www.ster.kuleuven.be/uaf
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include "uaf/client/configs/subscriptionconfig.h"


namespace uafc
{
    using namespace uaf;
    using std::string;
    using std::vector;
    using std::size_t;
    using std::stringstream;


    // Get a string representation
    // =============================================================================================
    string SubscriptionConfig::toString(const string& indent, size_t colon) const
    {
        stringstream ss;

        ss << indent << " - defaultSubscriptionSettings\n";
        ss << defaultSubscriptionSettings.toString(indent + "   ", colon) << "\n";

        ss << indent << " - specificSubscriptionSettings[]";
        if (specificSubscriptionSettings.size() > 0)
        {
            for (SpecificsMap::const_iterator it = specificSubscriptionSettings.begin();
                    it != specificSubscriptionSettings.end();
                    ++it)
            {
                ss << indent << "   " << " - specificSubscriptionSettings['" << it->first << "']\n";
                ss << it->second.toString(indent + "      ", colon);
                if (std::distance(it, specificSubscriptionSettings.end()) > 1)
                    ss << "\n";
            }
        }

        return ss.str();
    }

}
